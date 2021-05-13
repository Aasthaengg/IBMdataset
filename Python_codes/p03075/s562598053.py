list = [int(input()) for i in range(5)]
K = int(input())
print("Yay!" if max(list)-min(list) <= K else ":(")