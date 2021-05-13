s = input()
cnt = 0
for i in range(2,len(s)-1,2):
    s_1 = s[:(len(s)-i)//2 ]
    s_2 = s[(len(s)-i)//2 :len(s)-i]
    
    if s_1 == s_2:
        print(len(s) - i)
        cnt = 1
        break
if cnt == 0:
    print(2)