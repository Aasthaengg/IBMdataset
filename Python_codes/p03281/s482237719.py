N = int(input())
count_all = 0
def count_yakusuu(N):
    count = 0
    for i in range(3, int(N/3)+1):
        if N % i == 0:
            count += 1
    if count == 6:
        return True
    else:
        return False
for k in range(N+1):
    if k % 2 == 1:
        if count_yakusuu(k):
            count_all += 1
print(count_all)