abc = list(map(int, input().split()))
abc.sort()

bc = abc[2] - abc[1]
ab = abc[1] - abc[0]

print(bc + ab//2 if ab%2==0 else bc + ab//2 + 2)