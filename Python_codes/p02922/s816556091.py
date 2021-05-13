A, B = [int(i) for i in input().split()]
socket_count = A
result = 1

if B == 1:
    print(0)
else:
    while socket_count <= B:
        if socket_count == B:
            break
        else:
            socket_count += (A - 1)
            result += 1
    print(result)