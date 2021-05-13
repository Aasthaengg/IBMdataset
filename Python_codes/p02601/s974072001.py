A, B, C = map(int, input().split())
K = int(input())
count = 0
j = 1


while(A>=B):
    if(count<K):
        B *= 2
        count += 1
    else:
        j = 0
        break
while(C<=B):
    if(count<K):
        C *= 2
        count += 1
    else:
        j=0
        break
    
if(j == 1):
    print('Yes')
else:
    print('No')