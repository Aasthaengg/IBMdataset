s = input()
x, y = [ int(v) for v in input().split() ]

f_length_list = list(map(len,s.split("T")))

x_point_set = set([0])
y_point_set = set([0])

for i, v in enumerate(f_length_list):
    new_point_set = set([])
    if i % 2 == 0:
        if i == 0:
            new_point_set.add(v)
        else:
            for j in x_point_set:
                new_point_set.add(j+v)
                new_point_set.add(j-v)
        x_point_set = new_point_set

    elif i % 2 != 0:
        for j in y_point_set:
            new_point_set.add(j+v)
            new_point_set.add(j-v)
        y_point_set = new_point_set

if x in x_point_set and y in y_point_set:
    ans = "Yes"
else:
    ans = "No"
print(ans)