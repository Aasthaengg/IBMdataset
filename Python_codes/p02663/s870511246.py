h1, m1, h2, m2, k = [int(i) for i in input().split()]

awake = 60*h2+m2 - (60*h1+m1) - k
print(awake)