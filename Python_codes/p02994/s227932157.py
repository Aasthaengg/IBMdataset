n,l = map(int,input().split())
aji = [l+i for i in range(n)]
mn= 100
for i in range(n):
    mn= min(mn,abs(aji[i]))
if mn in aji:del aji[aji.index(mn)]
else:del aji[aji.index(-mn)]
print(sum(aji))