n,m,x = map(int, input().split())
a_list = list(map(int, input().split()))

former = []
latter = []

for i in range(len(a_list)):
    if a_list[i] < x:
        former.append(a_list[i])
    else:
        latter.append(a_list[i])
print(min(len(former), len(latter)))