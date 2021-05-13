S = input()
T = input()
answer = 'No'
rotationS = S
for i in range(len(S)):
    rotationS = rotationS[-1] + rotationS[0:-1]
    if rotationS == T:
        answer = 'Yes'
        break
print(answer)