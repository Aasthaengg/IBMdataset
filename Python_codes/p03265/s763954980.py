x1, y1, x2, y2 = map(int, input().split())

vec = (x2 - x1, y2 - y1)

vec2 = (-vec[1], vec[0])
vec3 = (-vec2[1], vec2[0])

x3, y3 = (x2 + vec2[0], y2 + vec2[1])
x4, y4 = (x3 + vec3[0], y3 + vec3[1])

print(x3, y3, x4, y4)
