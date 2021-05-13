N = int(input())
Alist = list(map(int, input().split()))


def inverse(num):
    return 1/num


invAlist = []

for a in Alist:
    invAlist.append(inverse(a))


print(inverse(sum(invAlist)))
