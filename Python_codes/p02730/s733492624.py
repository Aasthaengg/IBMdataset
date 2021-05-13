S = input()
length = len(S)

def check_palin(s):
    num = len(s)
    for i in range(num // 2):
        if s[i] != s[num - i - 1]:
            return False
    return True

first = S[:(length - 1) // 2]
second = S[(length + 1) // 2:]
#print(first)
#print(second)

if check_palin(S) and check_palin(first) and check_palin(second):
    print("Yes")
else:
    print("No")
