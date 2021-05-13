n = int(input())

vec_x = (int(x) for x in input().split())
vec_y = (int(x) for x in input().split())

# calc each abs
abs_vec = [abs(int(x) - int(y)) for x, y in zip(vec_x, vec_y)]

for p in range(1, 4):
    print(sum(x ** p for x in abs_vec) ** float(1 / p))

print(max(abs_vec))