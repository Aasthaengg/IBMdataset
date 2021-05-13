def maxf(n):
    a = list(map(int, list(n)))
    for i, item in enumerate(a):
        if i == 0 and item != 9:
            if a[i+1:] == [9]*(len(a)-1):break
            a[i] -=1
            a[i+1:] = [9]*(len(a)-1)
            break
        elif item != 9:
            a[i-1] -= 1
            a[i:] = [9]*(len(a)-i)
            break
    return sum(a)

print(maxf(input()))
