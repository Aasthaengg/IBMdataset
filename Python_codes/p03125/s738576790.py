a , b = map(int, input().split())
yakusuu_list = []
for i in range(1,b+1):
    if b % i == 0:
        yakusuu_list.append(i)
if a in yakusuu_list:
    print(a + b)
else:
    print(b - a)
