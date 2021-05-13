n = int(input())

v = list(map(int,input().split()))

v.sort(reverse = True)

while len(v) > 1 :
    v.append((v.pop(-1) + v.pop(-1))/2)
    v.sort(reverse = True)

print(v[0])
