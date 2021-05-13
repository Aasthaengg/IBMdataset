A,B,C=map(int,input().split())#どれか１つでも偶数ならばans=0
l=[A,B,C]
for i in range(3):
    if l[i]%2==0:
        print(0)
        exit()
#以下すべて奇数の場合）
x=(A//2 +1)*B*C-(A//2)*B*C
y=A*(B//2 +1)*C-A*(B//2)*C
z=A*B*(C//2 +1)-A*B*(C//2)
print(min(x,y,z))