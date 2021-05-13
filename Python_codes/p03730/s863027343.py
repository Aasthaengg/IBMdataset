a, b, c = map(int, input().split())

# if a % b == 0 and c != 0:
#     print('NO')
# else:
#     print('YES')

dic = {a%b:0}
now = a
while(1):
    now += a
    if now%b in dic:
        break
    else:
        dic[now%b]= 0

if c in dic:
    print('YES')
else:
    print('NO')
