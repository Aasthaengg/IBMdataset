# solution
import io

nim, mike = map(int, input().split())
k = mike - nim
print(k * (k + 1) // 2 - mike)