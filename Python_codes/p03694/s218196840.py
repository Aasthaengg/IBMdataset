result =0
n = int(input())
n2 = [int(i) for i in input().split()]
n2.sort()
print(n2[-1]-n2[0])
