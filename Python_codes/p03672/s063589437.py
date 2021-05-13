s = input()
m_len = len(s)-1
for i in range(len(s)):
    tmp = s[:m_len-i]
    if len(tmp)%2 != 0:
        continue
    if tmp[:len(tmp)//2] == tmp[len(tmp)//2:]:
        print(len(tmp))
        break