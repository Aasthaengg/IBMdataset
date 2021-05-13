'''
def num_div(n):
    cnt = 0
    for i in range(1, n+1, 2):
        if n % i == 0:
            cnt += 1
    return cnt

l = []
for i in range(1, 201):
    if num_div(i) == 0:
        l.append(i)
'''
l = [105, 135, 165, 189, 195]

n = int(input())

for i in range(5):
    if n < l[i]:
        print(i)
        exit()

print(5)