def operation(a,ops):
    ans = a[0]
    for i in range(3):
        if ops[i]=='+':
            ans += a[i+1]
        else:
            ans -= a[i+1]
    return ans

s = list(input())
a = [int(i) for i in s]
op = ['+','-']

for i in range(1<<3):
    ops = [op[1&(i>>j)] for j in range(3)]
    if operation(a,ops)==7:
        print("{}{}{}{}{}{}{}=7".format(a[0],ops[0],a[1],ops[1],a[2],ops[2],a[3]))
        break