N_str, q_str = raw_input().split()
N = int(N_str)
q = int(q_str)

A = []
B = []

for i in range(N):
    a = raw_input().split()
    A.append([a[0], int(a[1])])

total_time = 0
while A:
    name, time = A.pop(0)
    if time <= q:
        total_time += time 
        B.append("%s %d" % (name, total_time))
    else:
        time -= q
        A.append([name, time])
        total_time += q
print '\n'.join(B)