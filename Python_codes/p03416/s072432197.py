#ABC090-B
a,b = map(int,input().split())

def kaibun(n):
    flg = True
    for i in range(len(str(n))//2):
        if str(n)[i] != str(n)[-1-i]:
            flg = False
            break
            
    if flg:
        return True
    else:
        return False
    
cnt = 0
for i in range(a,b+1):
    if kaibun(i):
        cnt += 1
        
print(cnt)