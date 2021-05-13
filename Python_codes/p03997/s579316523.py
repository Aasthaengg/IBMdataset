def calc_trapezoid_area(top_length, under_length, height):    
    return (top_length + under_length) * height // 2

if __name__=='__main__':
    top_length, under_length, height = map(int, [input() for i in range(3)])
    print(calc_trapezoid_area(top_length, under_length, height))