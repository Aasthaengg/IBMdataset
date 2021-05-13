# solution
import io

data = int(input())
mike = 1 if data % 11 else 0
print((data // 11) * 2 + (data % 11) // 7 + mike)