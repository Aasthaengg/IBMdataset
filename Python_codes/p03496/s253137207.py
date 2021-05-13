N = int(input())
A = list(map(int,input().split()))

Amax = max(A)
Amin = min(A)
ans = []
if Amax >= -Amin:
    im = A.index(Amax)+1
    i = 2
    while i <= N:
        if A[i-2] > A[i-1]:
            ans.append(str(im) + " " + str(i))
            A[i-1] += Amax
            if Amax < A[i-1]:
                im = i
                Amax = A[i-1]
        else:
            i += 1
else:
    im = A.index(Amin)+1
    i = N-1
    while i >= 1:
        if A[i-1] > A[i]:
            ans.append(str(im) + " " + str(i))
            A[i-1] += Amin
            if Amin > A[i-1]:
                im = i
                Amin = A[i-1]
        else:
            i -= 1
print(len(ans))
for out in ans:
    print(out)