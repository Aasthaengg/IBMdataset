# coding: utf-8
# user: herp_sy

def quicksort(seq):
    if len(seq) < 1:
        return seq
    pivot = seq[0]
    left = []
    right = []
    for x in range(1, len(seq)):
        if seq[x] <= pivot:
            left.append(seq[x])
        else:
            right.append(seq[x])
    left = quicksort(left)
    right = quicksort(right)
    foo = [pivot]
    return (left + foo + right)

# , = map(int, input.split())
#  = int(input())

cnt = 0
cf2016 = "CODEFESTIVAL2016"
s = input()
for i in range(0,len(cf2016)):
    if cf2016[i] != s[i]:
        cnt = cnt + 1
print(cnt)