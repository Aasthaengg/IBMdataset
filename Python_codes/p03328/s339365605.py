A, B = map(int, input().split())
 
diff = B - A
height_A = diff * (diff - 1) // 2
 
ans = height_A - A
 
print(ans)