H, W, K = map(int, input().split())
Matrix = list()
answer = 0

def main(H, W, Matrix, i, K):
    Blacl_Count = 0 
    Bin = format(i, '12b')
    for a, line in enumerate(Matrix):
        for b, raw in enumerate(line):
            if Bin[-(a+1)] == '1' or Bin[-(b+H+1)] == '1':
                continue
            elif raw == '#':
                Blacl_Count += 1
    if Blacl_Count == K:
        return 1
    else:
        return 0

for h in range(H):
    line = input()
    Matrix.append(line)

iteration = 2**(H+W)

for i in range(iteration):
    answer += main(H, W, Matrix,i, K)

print(answer)