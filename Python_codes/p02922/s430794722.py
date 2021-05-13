A, B = [int(i) for i in input().split()]
result = 1
require_socket = B - A

result += require_socket // (A - 1)
if (require_socket / (A - 1)).is_integer() is False:
    result += 1

print(result)