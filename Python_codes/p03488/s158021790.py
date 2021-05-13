def main():
    order = [len(el) for el in list(map(str, input().rstrip().split("T")))]
    x_points = {order[0]}
    y_points = {0}
    for val in order[2::2]:
        plus_val = {x + val for x in list(x_points)}
        minus_val = {x - val for x in list(x_points)}
        x_points = plus_val | minus_val
    for val in order[1::2]:
        plus_val = {y + val for y in list(y_points)}
        minus_val = {y - val for y in list(y_points)}
        y_points = plus_val | minus_val
    target_x, target_y = map(int, input().split())
    if target_x in x_points and target_y in y_points:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
