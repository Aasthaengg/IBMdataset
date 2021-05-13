input_line = input()
A,B = [int(s) for s in input_line.split(' ') if s]

def answer(A,B):
    return A+B if B % A == 0 else B-A

print(answer(A,B))