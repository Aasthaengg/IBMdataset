H,W = map(int,input().split())
char = [0 for _ in range(26)]
rem = [0,0,0,0]

for i in range(H):
    a = input()
    for j in range(W):
        char[ord(a[j])-97] += 1

for i in range(26):
    rem[char[i]%4] += 1
    
if H%2==0 and W%2==0:
    print('Yes' if rem[0]==26 else 'No')
    
elif H%2!=0 and W%2!=0:
    print('Yes' if rem[1]+rem[3]==1 and rem[2]+rem[3]<=(H-1)//2+(W-1)//2 else 'No')
    
else:
    print('Yes' if rem[1]+rem[3]==0 and rem[2]<=(H%2)*(W//2)+(W%2)*(H//2) else 'No')
