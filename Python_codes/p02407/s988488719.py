num=int(input())
input_data = [int(i) for i in input().split()]
input_data.reverse()
print(" ".join(str(b) for b in input_data))