A, B = map(int, input().split())

answer = 'IMPOSSIBLE'
start = (A + B) // 2 - 1
end = (A + B) // 2 + 1


for i in range(start, end+1):
    a = abs(A - i)
    b = abs(B - i)
    
    if a == b:
        answer = i
        break

print(answer)