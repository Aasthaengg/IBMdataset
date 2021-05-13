N = int(input())
L = list(map(int, input().split()))

L.sort(reverse = True)
i = j = k = 0
cnt = 0

while i<len(L)-2:
    j = i + 1
    while j<len(L)-1:
        k = j + 1
        if L[i] != L[j]:
            while k<len(L):
                if L[j] != L[k] and L[i] < L[j] + L[k]:
                    cnt += 1
                k += 1
        j += 1
    i += 1

print(cnt)
