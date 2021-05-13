N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))

q_1 = []
q_2 = []
q_3 = []

for i in P:
    if i <= A:
        q_1.append(i)
    elif A < i <= B:
        q_2.append(i)
    else:
        q_3.append(i)

print(min(len(q_1), len(q_2), len(q_3)))