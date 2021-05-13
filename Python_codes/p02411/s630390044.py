M, F, R = map(int, input().split())
while not (M == -1 and F == -1 and R == -1):
 if M == -1 or F == -1: print("F")
 elif M+F >= 80: print("A")
 elif M+F >= 65: print("B")
 elif M+F >= 50 or (M+F >= 30 and R >= 50): print("C")
 elif M+F >= 30: print("D")
 else: print("F")

 M, F, R = map(int, input().split())