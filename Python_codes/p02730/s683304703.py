def isPalindrome(string):
    flag = True
    len_string = len(string)
    if len_string == 1:
        return flag
    for i in range(len_string//2):
        if string[i] != string[-1-i]:
            flag = False
            break
    return flag

S = input()
len_s = len(S)
fro_s = S[:len_s//2]
if len_s % 2 == 0:
    bak_s = S[-len_s//2:]
else:
    bak_s = S[-len_s//2 + 1:]

if isPalindrome(S) and isPalindrome(fro_s) and isPalindrome(bak_s):
    print('Yes')
else:
    print('No')