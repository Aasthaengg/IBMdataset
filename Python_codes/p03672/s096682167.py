s = input()
len_s = len(s)
is_ok = False
while(is_ok == False):
    len_s -= 2
    word = s[:len_s]
    if word[:len_s // 2] == word[len_s // 2 :]:
        is_ok = True
    else:
        pass
print(len_s)