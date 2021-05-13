def digit_transform(N):
    if N == 0:  return "0"
    ans = ""
    while(N != 0):
        if N % -2 == 0:
            ans = "0" + ans
        else:
            ans = "1" + ans
            N -= 1
        N /= -2
    return ans

print(int(digit_transform(int(input()))))