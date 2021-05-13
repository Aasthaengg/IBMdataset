from collections import Counter
N = int(input())
numbers = [int(i) for i in input().split()]

o = Counter(numbers[::2]).most_common()
e = Counter(numbers[1::2]).most_common()

if o[0][0] == e[0][0]:
    if len(o) == 1:
        output = N // 2
    else :
        e1, e2 = e[0][1], e[1][1]
        o1, o2 = o[0][1], o[1][1]
        
        output = min(N-e1-o2, N-e2-o1)
else :
    output = N - o[0][1] - e[0][1]

print(output)