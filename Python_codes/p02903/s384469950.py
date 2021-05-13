H, W, A, B = map(int, input().split())

col1 = []
col2 = []

for _ in range(A):
    col1.append("0")
    col2.append("1")
    
for _ in range(W - A):
    col1.append("1")
    col2.append("0")
    
row1 = "".join(col1)  # 011
row2 = "".join(col2)  # 100

for _ in range(B):
    print(row1)
    
for _ in range(H - B):
    print(row2)