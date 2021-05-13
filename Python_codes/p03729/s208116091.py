A,B,C = map(list,input().split())
# Pythonの三項演算子の書き方、結構違和感ある
print('YES') if A[-1] == B[0] and B[-1] == C[0] else print('NO')