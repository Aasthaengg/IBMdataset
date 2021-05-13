s = input()
k = int(input())
ok = True
for i in range(k):
    if s[i] != "1":
        print(s[i])
        ok = False
        exit()
if ok:
    print(1)
    
    
