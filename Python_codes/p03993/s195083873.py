n = int(input())
a = [int(i) for i in input().split()]
ai = []

for i, j in enumerate(a):
    ai.append([i+1,j])
    ai[i].sort()

print(len(ai) - len(list(map(list,set(map(tuple, ai))))))

