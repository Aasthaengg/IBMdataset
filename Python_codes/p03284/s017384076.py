n,k=map(int,input().split())
bl = True
if n%k !=0:
    bl = False
print('0' if bl else '1')