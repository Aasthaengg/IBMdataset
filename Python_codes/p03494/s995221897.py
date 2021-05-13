N = int(input())
A = [int(n) for n in input().split()]

ans = 0

def func(array):
    for i in range(len(array)):
        if array[i]%2 != 0:
            return False
        else:
            array[i] = array[i]//2
    return True


while True:
    if len(A) == A.count(0):
        break
    if func(A):
        ans += 1
    else:
        break

print(ans)