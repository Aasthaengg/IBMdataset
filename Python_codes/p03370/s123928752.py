n, x = map(int, input().split())
material_needed = []
for _ in range(n):
    material_needed.append(int(input()))

rest_material = x - sum(material_needed)
min_donut_material = min(material_needed)

print(len(material_needed) + rest_material // min_donut_material)
