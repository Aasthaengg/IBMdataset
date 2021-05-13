ans=[1,2,3]
ab=[int(input()) for _ in range(2)]

print(*(set(ans)^set(ab)))